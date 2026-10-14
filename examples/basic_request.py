"""Minimal Gemini 4 Argon example using the official Google Gen AI SDK.

Requirements: Python 3.10+, google-genai, and a GEMINI_API_KEY environment variable.
"""
import os
import sys

from google import genai


def main() -> None:
    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("Set GEMINI_API_KEY to your Google AI Studio API key before running.")

    client = genai.Client()
    try:
        response = client.interactions.create(
            model="gemini-4-argon",
            input="Explain Python list comprehensions in two sentences, with one example.",
        )
        print(response.output_text or "No text response returned.")
    except Exception as exc:
        sys.exit(f"Gemini API request failed: {exc}")


if __name__ == "__main__":
    main()
