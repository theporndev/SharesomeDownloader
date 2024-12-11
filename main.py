import aiohttp
import asyncio
import argparse
from aiofiles import open as aio_open
from bs4 import BeautifulSoup


async def fetch_post(session, post_url):
    """
    Fetch the post and extract the video URL using BeautifulSoup.
    """
    try:
        async with session.get(post_url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                video = soup.find('video')
                if video:
                    return video.get('src')
                else:
                    return None
            else:
                return None
    except Exception:
        return None


async def download_video(session, video_url, downloads_dir="."):
    """
    Download the video from the extracted video URL and save to the specified directory.
    """
    try:
        filename = video_url.split("/")[-1]
        async with session.get(video_url) as response:
            if response.status == 200:
                async with aio_open(f"{downloads_dir}/{filename}", "wb") as f:
                    content = await response.read()
                    await f.write(content)
                return True  # Download successful
            else:
                return False
    except Exception:
        return False


async def get_video(post_url):
    """
    Main function to fetch the video URL and download it. Handles retries.
    """
    async with aiohttp.ClientSession() as session:
        for attempt in range(2):  # Retry up to 2 times
            video_url = await fetch_post(session, post_url)
            if video_url:
                success = await download_video(session, video_url)
                if success:
                    print(f"Download successful for: {post_url}")
                else:
                    print(f"Download failed for: {post_url}")
                return  # Exit once the process is completed
        print(f"Download failed for: {post_url}")


async def process_all_videos(urls):
    """
    Process all video URLs concurrently.
    """
    tasks = [get_video(url) for url in urls]  # Create a list of tasks for all URLs
    await asyncio.gather(*tasks)  # Run all tasks concurrently


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Download videos from given URLs.")
    parser.add_argument(
        "urls",
        nargs="*",  # Accept zero or more URLs
        help="The URLs of the videos to download",
    )
    args = parser.parse_args()

    # Use URLs from arguments if provided, otherwise fallback to input
    if args.urls:
        asyncio.run(process_all_videos(args.urls))  # Process multiple URLs concurrently
    else:
        post_url = input("Enter post URL: ")
        asyncio.run(process_all_videos([post_url]))


# Example usage
if __name__ == "__main__":
    main()