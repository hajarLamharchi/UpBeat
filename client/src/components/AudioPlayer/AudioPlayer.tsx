import SongInfo from "./SongInfo";
import AudioControls from "./AudioControls";
import VolumeControls from "./VolumeControls";
import playerContext from "../../context/playerContext";
import { useContext, useRef } from "react";

interface AudioPlayerProps {}

const AudioPlayer: React.FC<AudioPlayerProps> = ({}) => {
  const { currentSong, playlist } = useContext(playerContext);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  return (
    currentSong && (
      <footer className="fixed bottom-0 w-full max-w-screen-2xl">
        <div className="relative bg-clip-padding backdrop-filter backdrop-blur-md bg-opacity-30 border-x border-t border-slate-700  bg-gray-800 mx-2 text-white py-3 pb-4 px-4 rounded-t-lg flex justify-between items-center">
          <audio
            ref={audioRef}
            src={playlist[currentSong].preview_url}
            preload="metadata"
            autoPlay
          />
          <SongInfo />
          <AudioControls audioRef={audioRef} />
          <VolumeControls audioRef={audioRef} />
        </div>
      </footer>
    )
  );
};

export default AudioPlayer;
