import os
import sys
from youtube_transcript_api import YouTubeTranscriptApi
import openai
from openai import OpenAI


def main():
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    if not openai.api_key:
        print("Error: OPENAI_API_KEY not found in environment.")
        return

    if len(sys.argv) < 2:
        print("Usage: transcript.py <video_id>")
        return

    video_id = sys.argv[1]
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ja', 'en'])
        all_text = "\n".join([item['text'] for item in transcript_list])
    except Exception as e:
        print(f"Failed to get transcript: {e}")
        return

    client = OpenAI()

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "あなたは優秀な解説者です。"},
                {"role": "user", "content": f"次のテキストを解説してください。\n{all_text}"}
            ],
            response_format={
                "type": "text"
            },
            temperature=0.2,
            max_completion_tokens=4096,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            store=False
        )
        summary = completion.choices[0].message.content
        print("===== 要約結果 =====")
        print(summary)
    except Exception as e:
        print(f"Failed to summarize: {e}")


if __name__ == "__main__":
    main()
