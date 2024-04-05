import { FaPlay } from "react-icons/fa";
import { FaPause } from "react-icons/fa6";
import { IoIosSkipForward } from "react-icons/io";
import { IoIosSkipBackward } from "react-icons/io";
import { FaShuffle } from "react-icons/fa6";
import { FiRepeat } from "react-icons/fi";
import { LuRepeat1 } from "react-icons/lu";
import { SliderHover } from "../SliderHover";
import { useContext, useEffect, useState, useRef } from "react";
import playerContext from "../../context/playerContext";

interface AudioControlsProps {
  audioRef: React.RefObject<any | null>;
}

const AudioControls: React.FC<AudioControlsProps> = ({ audioRef }) => {
  const [duration, setDuration] = useState("0:00");
  const [currentTime, setCurrentTime] = useState(0);
  const {
    togglePlay,
    isPlaying,
    setNextSong,
    setPrevSong,
    toggleShuffle,
    isShuffle,
    isRepeat,
    isRepeatOnce,
    toggleRepeat,
    toggleRepeatOnce,
    currentSong,
  } = useContext(playerContext);

  const animationRef = useRef<any>();

  const calculateTime = (secs: number) => {
    const minutes = Math.floor(secs / 60);
    const returnedMinutes = minutes < 10 ? `0${minutes}` : `${minutes}`;
    const seconds = Math.floor(secs % 60);
    const returnedSeconds = seconds < 10 ? `0${seconds}` : `${seconds}`;
    return `${returnedMinutes}:${returnedSeconds}`;
  };

  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.onloadedmetadata = () => {
        const secondes = Math.floor(audioRef.current.duration);
        setDuration(calculateTime(secondes));
      };
      animationRef.current = requestAnimationFrame(whilePlaying);
    }

    return () => {
      if (audioRef.current) {
        audioRef.current.onloadedmetadata = null;
      }
    };
  }, []);

  useEffect(() => {
    audioRef.current?.addEventListener("ended", hangleEnded);
    return () => {
      audioRef.current?.removeEventListener("ended", hangleEnded);
    };
  }, [isRepeatOnce, isRepeat, currentSong]);

  const hangleEnded = () => {
    if (!isRepeatOnce && !isRepeat) {
      setNextSong();
    } else {
      setCurrentTime(0);
      audioRef.current?.play();
      if (isRepeatOnce) {
        toggleRepeatOnce();
      }
    }
  };

  const togglePlayPause = () => {
    if (isPlaying) {
      audioRef.current?.pause();
      cancelAnimationFrame(animationRef.current);
    } else {
      audioRef.current?.play();
      animationRef.current = requestAnimationFrame(whilePlaying);
    }
  };

  const whilePlaying = () => {
    setCurrentTime(audioRef?.current?.currentTime);
    animationRef.current = requestAnimationFrame(whilePlaying);
  };
  return (
    <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 flex flex-col items-center gap-2 mt-[2px]">
      <div className="flex items-center gap-5">
        <div>
          {isShuffle ? (
            <FaShuffle
              className="text-lg cursor-pointer text-green-500"
              onClick={() => toggleShuffle()}
            />
          ) : (
            <FaShuffle
              className="text-lg cursor-pointer"
              onClick={() => toggleShuffle()}
            />
          )}
        </div>
        <IoIosSkipBackward
          className="text-2xl cursor-pointer"
          onClick={() => setPrevSong()}
        />
        <div
          className="w-10 aspect-square text-gray-800 bg-white rounded-full flex items-center justify-center cursor-pointer"
          onClick={() => {
            togglePlay();
            togglePlayPause();
          }}
        >
          {isPlaying ? (
            <FaPause className="text-2xl" />
          ) : (
            <FaPlay className="text-xl" />
          )}
        </div>
        <IoIosSkipForward
          className="text-2xl cursor-pointer"
          onClick={() => setNextSong()}
        />
        <div onClick={() => toggleRepeat()}>
          {isRepeatOnce ? (
            <LuRepeat1 className="text-lg cursor-pointer text-green-500" />
          ) : isRepeat ? (
            <FiRepeat className="text-lg cursor-pointer text-green-500" />
          ) : (
            <FiRepeat className="text-lg cursor-pointer text-gray-300" />
          )}
        </div>
      </div>
      <div className="flex items-center gap-2">
        <div className="text-xs select-none text-gray-300">
          {calculateTime(currentTime)}
        </div>
        <div className="w-96">
          <SliderHover
            barStyles={{ backgroundColor: "#228BE6" }}
            trackRef={audioRef}
            value={(currentTime / audioRef.current?.duration) * 100 || 0}
            setCurrentTime={(time: number) => setCurrentTime(time)}
            size={5}
          />
        </div>
        <div className="text-xs select-none text-gray-300">
          {duration || "0:00"}
        </div>
      </div>
    </div>
  );
};

export default AudioControls;
