import { CiHeart } from "react-icons/ci";
import { FaHeart } from "react-icons/fa";
import "./SongInfo.css";
import playerContext from "../../context/playerContext";
import { useContext } from "react";
import { Song } from "../../global.d";

interface SongInfoProps {}

const SongInfo: React.FC<SongInfoProps> = ({}) => {
  const { currentSong, playlist, likeSong } = useContext(playerContext);

  return (
    <div className="flex items-center gap-3">
      <img
        src={playlist[currentSong]?.album?.images[2]?.url}
        alt={playlist[currentSong]?.name}
        className="w-14 aspect-square rounded-sm"
      />
      <div className="min-w-12 flex flex-col gap-1">
        <div className="text-sm font-semibold">
          {playlist[currentSong]?.name}
        </div>
        <div className="text-xs text-gray-300">
          {playlist[currentSong]?.artists
            .map((artist: any) => artist.name)
            .join(", ")}{" "}
        </div>
      </div>
      <div className="text-lg">
        <div
          className="text-2xl cursor-pointer mx-auto"
          onClick={() => likeSong(playlist[currentSong]?.id)}
        >
          {playlist[currentSong]?.isLiked ? (
            <FaHeart className="text-red-500" />
          ) : (
            <CiHeart />
          )}
        </div>
      </div>
    </div>
  );
};

export default SongInfo;
