import sys
from youtube_transcript_api import YouTubeTranscriptApi


def main():
    if len(sys.argv) < 2:
        print("Usage: transcript.py <video_id>")
        return

    video_id = sys.argv[1]
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        all_text = "\n".join([item['text'] for item in transcript_list])
        print(all_text)
    except Exception as e:
        print(f"Failed to get transcript: {e}")


if __name__ == "__main__":
    main()
