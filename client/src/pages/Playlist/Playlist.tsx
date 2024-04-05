import { useNavigate, useParams } from "react-router-dom";
import SideNavbar from "../../components/SideNavbar/SideNavbar";
import { useContext, useEffect, useState } from "react";
import axios from "axios";
import { IoIosArrowBack, IoIosArrowForward } from "react-icons/io";
import { FaPlay } from "react-icons/fa";
import { CiHeart } from "react-icons/ci";
import { FaHeart } from "react-icons/fa";
import playerContext from "../../context/playerContext";
import { Song } from "../../global";

interface PlaylistsProps {
  isLoggedIn: boolean;
  usename: string;
}

function Playlist({ isLoggedIn, usename }: PlaylistsProps) {
  const { id } = useParams<{ id: string }>();
  console.log(id);

  // const [playlist, setPlaylist] = useState<any>([]);
  const [songs, setSong] = useState<any>([]);
  let history = useNavigate();
  const { setCurrentSong, currentSong, setPlaylist } =
    useContext(playerContext);

  // const currentSongIndex = playlist.findIndex(
  //   (song: Song) => song.id === currentSong
  // );

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

  useEffect(() => {
    axios
      .get(`https://upbeat-server.onrender.com/api/v1/playlist/${id}/tracks`)
      .then((response) => {
        console.log(response.data);
        response.data.map((item: any) => {
          // console.log(item);
          setSong((prev: any) => [...prev, item.track]);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="homepage-container relative">
      <SideNavbar isLoggedIn={isLoggedIn} />
      <div className="w-[90%] h-svh ml-1 p-5 overflow-hidden">
        <div className="relative bg-clip-padding backdrop-filter backdrop-blur-md bg-opacity-30 border border-slate-700  bg-gray-800 mx-2 text-white rounded-lg w-full h-[94vh]">
          <header className="fixed top-0 left-0 w-full z-10 backdrop-filter backdrop-blur-sm border-b border-slate-600 py-4 px-6 bg-clip-padding">
            <div className="navigate-container">
              <button className="bg-gray-700 p-2 rounded-lg hover:bg-gray-600 transition-colors duration-100 ease-in-out">
                <IoIosArrowBack onClick={() => history(-1)} />
              </button>
              <button>
                <IoIosArrowForward onClick={() => history(1)} />
              </button>
            </div>
          </header>
          <div className="relative z-0 w-full h-full overflow-auto">
            <div
              style={{
                background:
                  "linear-gradient(180deg, #4E5B6F 0%, #4E5B6F 70%, transparent 100%, transparent 100%)",
              }}
              className="absolute top-0 left-0 w-full min-h-[40rem] -z-10 rounded-md"
            ></div>
            <header className="flex justify-between items-center mx-5 translate-y-1 shadow-xl">
              <div className="overflow-hidden w-full">
                <div className="bg-gradient-to-bl from-slate-600 bg-slate-400 flex min-h-80 mt-5 items-end rounded-md">
                  <div className="flex gap-5 items-end p-5">
                    <div className="relative w-56 aspect-square rounded-md overflow-hidden group cursor-pointer shadow-2xl">
                      <img
                        src="https://picsum.photos/200/300"
                        alt="album cover"
                        className="absolute top-0 left-0 w-full h-full object-cover"
                      />
                    </div>
                    <div className="flex flex-col gap-2">
                      <span>Playlist</span>
                      <h1 className="text-8xl font-bold">Maga Hit Mix</h1>
                      <p className="text-gray-900 text-opacity-85">
                        A mega mix of 75 favorites from the last few years!
                      </p>

                      {/* add playlist total songs, likes, total duration sparated by a dot */}
                      <div className="flex gap-2 text-gray-50 text-sm">
                        <span>7,000 likes</span>
                        <span>•</span>
                        <span>75 songs</span>
                        <span>•</span>
                        <span>about 1.5 hr</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </header>
            <div className="px-5 bg-slate-800 bg-opacity-50">
              <section className="px-5 py-5">
                <div className="flex justify-between items-center w-full">
                  <div className="flex gap-5 items-center mt-3">
                    <button className="bg-fuchsia-500 text-white text-xl p-5 rounded-full">
                      <FaPlay />
                    </button>
                    <button className="text-white text-4xl">
                      <CiHeart />
                    </button>
                  </div>
                  <button className="text-white text-2xl">...</button>
                </div>
              </section>
              <section className="px-5">
                <div className="px-2 py-5">
                  <table className="w-full overflow-x-hidden">
                    <thead>
                      <tr className="text-left text-white">
                        <th className="px-2 py-2 hidden sm:table-cell">#</th>
                        <th className="px-4 py-2">Title</th>
                        <th className="px-4 py-2 hidden md:table-cell">
                          Album
                        </th>
                        <th className="px-4 py-2 hidden xl:table-cell">
                          Release Date
                        </th>
                        <th className="px-4 py-2 hidden lg:table-cell"></th>
                        <th className="px-4 py-2">
                          <svg
                            data-encore-id="icon"
                            role="img"
                            aria-hidden="true"
                            viewBox="0 0 16 16"
                            className="text-white fill-current w-4 h-4"
                          >
                            <path d="M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13zM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8z"></path>
                            <path d="M8 3.25a.75.75 0 0 1 .75.75v3.25H11a.75.75 0 0 1 0 1.5H7.25V4A.75.75 0 0 1 8 3.25z"></path>
                          </svg>
                        </th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-700">
                      {[...Array(20)].map((_, i) => (
                        <tr
                          key={i}
                          style={
                            currentSong === i
                              ? { backgroundColor: "#374151" }
                              : {}
                          }
                          className="hover:bg-gray-700 cursor-pointer group"
                          onClick={() => {
                            setPlaylist(songs);
                            setCurrentSong(i);
                          }}
                        >
                          <td className="px-2 py-2 text-gray-400 hidden sm:table-cell">
                            {i + 1}
                          </td>
                          <td className="px-4 py-2 flex items-center">
                            <div className="w-14 relative rounded-lg group-hover:scale-105 transition-transform duration-300 ease-in-out">
                              <img
                                src={songs[i]?.album.images[2].url}
                                alt="song"
                                className="w-14 aspect-square rounded-lg group-hover:filter group-hover:brightness-75 transition-all duration-300 ease-in-out"
                              />
                              {/* Add play icon over img on hover */}
                              <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-opacity duration-300 ease-in-out">
                                <FaPlay className="text-2xl text-fuchsia-400" />
                              </div>
                            </div>
                            <div className="ml-4">
                              <h3 className="text-white font-bold md:max-w-60 5xl:max-w-72 truncate">
                                {songs[i]?.name}
                              </h3>
                              <p className="text-gray-400 text-sm md:max-w-60 5xl:max-w-72 truncate">
                                {songs[i]?.artists
                                  .map((artist) => artist.name)
                                  .join(", ")}
                              </p>
                            </div>
                          </td>
                          <td className="px-4 py-2 text-gray-400 hidden md:table-cell  md:max-w-40 5xl:max-w-60 truncate">
                            {songs[i]?.name}
                          </td>
                          <td className="px-4 py-2 text-gray-400 hidden xl:table-cell">
                            {songs[i]?.album.release_date &&
                              formatDate(songs[i]?.album.release_date)}
                          </td>
                          <td className="px-4 py-2 text-lg hidden lg:table-cell">
                            <div
                              className="text-2xl invisible group-hover:visible cursor-pointer mx-auto "
                              // onClick={() =>
                              //   likeSong(playlist[currentSongIndex]?.id)
                              // }
                            >
                              {false ? (
                                <FaHeart className="text-red-500" />
                              ) : (
                                <CiHeart className="hover:text-red-500 transition-colors duration-200 ease-in-out" />
                              )}
                            </div>
                          </td>
                          <td className="px-4 py-2 text-gray-400">3:45</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </section>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Playlist;
