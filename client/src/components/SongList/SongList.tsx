import { useContext } from "react";
import ListContainer from "../ListContainer/ListContainer";
import { CiHeart } from "react-icons/ci";
import { FaHeart } from "react-icons/fa";
import playerContext from "../../context/playerContext";
import { Song } from "../../global";
import { FaPlay } from "react-icons/fa";

interface SongListProps {
  songs: any[] | [];
}

function formatDate(inputDate: string) {
  const months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const [year, month, day] = inputDate?.split("-");
  const formattedDate = `${parseInt(day, 10)} ${
    months[parseInt(month, 10) - 1]
  } ${year}`;
  return formattedDate;
}

function SongList({ songs = [] }: SongListProps) {
  const { currentSong, playlist, likeSong } = useContext(playerContext);

  const currentSongIndex = playlist.findIndex(
    (song: Song) => song.id === currentSong
  );
  return (
    <ListContainer
      title="You may also like"
      id="spotify:playlist:37i9dQZF1DWZCOSaet9tpB"
    >
      <div className="grid lg:grid-cols-2 gap-y-2 gap-x-4 px-2 py-5">
        {[...Array(6)].map((_, i) => (
          <div key={i} className="@container">
            <div className="@container bg-gray-800 p-2 @xl:px-4 rounded-lg flex justify-between items-center group hover:bg-gray-700 transition-colors duration-300 ease-in-out cursor-pointer">
              <div className="flex gap-4 items-center @xl:basis-1/3">
                <span className="text-gray-400 hidden @xl:block">{i + 1}</span>
                <div className="w-14 relative rounded-lg group-hover:scale-105 transition-transform duration-300 ease-in-out">
                  <img
                    src={songs[i]?.images[2].url}
                    alt="song"
                    className="w-14 aspect-square rounded-lg group-hover:filter group-hover:brightness-75 transition-all duration-300 ease-in-out"
                  />
                  {/*  Add play icon over img on hover   */}
                  <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 ease-in-out">
                    <FaPlay className="text-2xl text-fuchsia-400" />
                  </div>
                </div>
                <div>
                  <h3 className="text-white font-bold max-w-60 truncate">
                    {songs[i]?.name}
                  </h3>
                  <p className="text-gray-400 text-sm truncate">
                    {songs[i]?.artists
                      .map((artist: any) => artist.name)
                      .join(", ")}
                  </p>
                </div>
              </div>
              <div className="hidden @xl:block">
                {/* add album name */}
                <span className="text-gray-400">{songs[i]?.name}</span>
              </div>
              <div className="hidden @3xl:block">
                {/* convert date to this format 27 Nov 2023 */}
                <span className="text-gray-400">
                  {songs[i]?.release_date && formatDate(songs[i]?.release_date)}
                </span>
              </div>
              <div className="flex gap-4">
                <div className="text-lg hidden @xl:block">
                  <div
                    className="text-2xl cursor-pointer mx-auto"
                    onClick={() => likeSong(playlist[currentSongIndex]?.id)}
                  >
                    {playlist[currentSongIndex]?.isLiked ? (
                      <FaHeart className="text-red-500" />
                    ) : (
                      <CiHeart className="hover:text-red-500 transition-colors duration-200 ease-in-out" />
                    )}
                  </div>
                </div>
                <span className="text-gray-400">{songs[i]?.duration_ms}</span>
                <button className="text-white group-hover:text-gray-400 transition-colors duration-300 ease-in-out @xl:hidden">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M9 5l7 7-7 7"
                    />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </ListContainer>
  );
}

export default SongList;
