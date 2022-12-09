import os
import sys
from pathlib import Path

import pandas as pd
from tqdm import tqdm
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

LINK_BASE = "https://youtu.be/"
SAVE_DIR = Path("./", "videos")


def download_video_by_id(yt_id: str, save_dir: Path, save_filename: str):
    link = LINK_BASE + yt_id
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4'). \
        order_by('resolution'). \
        desc(). \
        first(). \
        download(output_path=save_dir, filename=f"{save_filename}.mp4")


def crop_video(in_path: Path, out_path: Path, start_time: float, end_time: float, delete_orig=False):
    sys.stdout = open(os.devnull, 'w')
    ffmpeg_extract_subclip(
        filename=in_path,
        t1=start_time,
        t2=end_time,
        targetname=out_path
    )

    if delete_orig:
        in_path.unlink()
    sys.stdout = sys.__stdout__


def main(pattern="dancing"):
    for stage in ['train', 'validate']:
        labels_filename = f"{stage}.csv"
        df = pd.read_csv(labels_filename)
        target_df = df[df['label'].str.contains(pattern)]

        for index, row in tqdm(target_df.iterrows(), f"Downloading {stage}", total=len(target_df.index)):
            yt_id = row['youtube_id']
            start_time = float(row['time_start'])
            end_time = float(row['time_end'])
            full_video_name = f"tmp_{yt_id}"
            full_video_path = SAVE_DIR / f"{full_video_name}.mp4"
            cropped_video_path = SAVE_DIR / f"{yt_id}.mp4"

            if not cropped_video_path.is_file():
                try:
                    download_video_by_id(
                        yt_id=yt_id,
                        save_dir=SAVE_DIR,
                        save_filename=full_video_name
                    )
                    crop_video(
                        in_path=full_video_path,
                        out_path=cropped_video_path,
                        start_time=start_time,
                        end_time=end_time,
                        delete_orig=True
                    )
                except KeyboardInterrupt:
                    return
                except:
                    target_df.drop([index])

        target_df.to_csv(f"dance-{stage}.csv")


if __name__ == "__main__":
    main()
