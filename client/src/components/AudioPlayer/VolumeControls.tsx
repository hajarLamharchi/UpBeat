import { FaVolumeUp } from "react-icons/fa";
import { FaVolumeMute } from "react-icons/fa";
import { CiMaximize1 } from "react-icons/ci";
import { SliderHover } from "../SliderHover";
import { useState } from "react";

interface VolumeControlsProps {
  audioRef: React.RefObject<any>;
}

function VolumeControls({ audioRef }: VolumeControlsProps) {
  const [mute, setMute] = useState(false);
  const handleVolumeChange = (value: number) => {
    audioRef.current.volume = value;
    if (value > 0) {
      audioRef.current.muted = false;
      setMute(false);
    } else {
      audioRef.current.muted = true;
      setMute(true);
    }
  };

  const handleMute = () => {
    audioRef.current.muted = !audioRef.current.muted;
    setMute(audioRef.current.muted);
  };

  return (
    <div className="flex items-center gap-3">
      <div onClick={handleMute}>
        {!mute ? (
          <FaVolumeUp className="text-lg cursor-pointer" />
        ) : (
          <FaVolumeMute className="text-lg cursor-pointer" />
        )}
      </div>
      <div className="w-20">
        <SliderHover
          barStyles={{ backgroundColor: mute ? "transparent" : "#228BE6" }}
          trackRef={audioRef}
          size={4}
          onVolumeChange={handleVolumeChange}
        />
      </div>
      <CiMaximize1 className="text-lg cursor-pointer" />
    </div>
  );
}

export default VolumeControls;
