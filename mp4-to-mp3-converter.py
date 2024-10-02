import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_file, output_file):
    """
    Convert an MP4 file to MP3.
    
    :param input_file: Path to the input MP4 file
    :param output_file: Path to the output MP3 file
    """
    try:
        # Load the video file
        video = VideoFileClip(input_file)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to an MP3 file
        audio.write_audiofile(output_file)
        
        # Close the video file
        video.close()
        
        print(f"Conversion complete: {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Get the input MP4 file path
    input_file = input("Enter the path to the MP4 file: ").strip()
    
    # Check if the input file exists
    if not os.path.exists(input_file):
        print("Error: The specified input file does not exist.")
        return
    
    # Get the output MP3 file path
    output_file = input("Enter the path for the output MP3 file: ").strip()
    
    # Add .mp3 extension if not provided
    if not output_file.lower().endswith('.mp3'):
        output_file += '.mp3'
    
    # Perform the conversion
    convert_mp4_to_mp3(input_file, output_file)

if __name__ == "__main__":
    main()
