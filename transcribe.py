import argparse
from faster_whisper import WhisperModel
import os

def main():
    parser = argparse.ArgumentParser(
        description="Local audio transcription with Faster-Whisper (timestamps included)"
    )
    parser.add_argument("audio_file", help="Path to your audio/video file (mp3, wav, m4a, mp4, etc.)")
    parser.add_argument("--model", default="small", choices=["tiny", "base", "small", "medium", "large", "large-v3"],
                        help="Model size (larger = more accurate, slower). Default: small")
    parser.add_argument("--device", default="auto", choices=["auto", "cpu", "cuda"],
                        help="Device to use (auto = GPU if available)")
    parser.add_argument("--output", default=None, help="Output text file (default: audio_filename.txt)")
    parser.add_argument("--plain-only", action="store_true",
                        help="Only output plain text (no timestamps)")
    args = parser.parse_args()

    # Load model (downloads automatically on first run)
    print(f"Loading {args.model} model on {args.device}...")
    model = WhisperModel(
        args.model,
        device=args.device if args.device != "auto" else "cuda" if torch.cuda.is_available() else "cpu",
        compute_type="float16" if (args.device == "cuda" or (args.device == "auto" and torch.cuda.is_available())) else "int8"
    )

    print(f"Transcribing {args.audio_file}...")
    segments, info = model.transcribe(
        args.audio_file,
        beam_size=5,
        word_timestamps=True,      # Enables word-level timestamps
        language="en",             # Force English (remove this line for auto-detect)
        vad_filter=True            # Better handling of silence
    )

    print(f"\nDetected language: {info.language} (probability: {info.language_probability:.2%})")
    print(f"Transcription duration: {info.duration:.1f} seconds\n")

    full_text = []
    detailed_output = []

    for segment in segments:
        # Segment-level timestamp
        start = segment.start
        end = segment.end
        text = segment.text.strip()

        detailed_output.append(f"[{start:.2f}s → {end:.2f}s] {text}")
        full_text.append(text)

        # Optional: show word-level timestamps too
        if not args.plain_only and segment.words:
            words_str = "   ".join(
                f"{word.word.strip()} [{word.start:.1f}s]" for word in segment.words
            )
            detailed_output.append(f"    ↳ Words: {words_str}")

    # Plain English text
    plain_transcript = "\n".join(full_text)

    # Choose output file name
    if not args.output:
        base = os.path.splitext(args.audio_file)[0]
        args.output = f"{base}_transcript.txt"

    # Write output
    with open(args.output, "w", encoding="utf-8") as f:
        if args.plain_only:
            f.write(plain_transcript)
            print("✅ Saved plain text to", args.output)
        else:
            f.write("\n".join(detailed_output))
            f.write("\n\n=== PLAIN TEXT ===\n")
            f.write(plain_transcript)
            print("✅ Saved detailed transcript (with timestamps) to", args.output)

    # Also print to console
    print("\n" + "="*60)
    print("TRANSCRIPTION COMPLETE")
    print("="*60)
    print(plain_transcript)
    print("="*60)

if __name__ == "__main__":
    import torch  # only needed for device auto-detect
    main()