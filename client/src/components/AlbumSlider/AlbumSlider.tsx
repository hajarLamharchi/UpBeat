import "./AlbumSlider.css";
import ListContainer from "../ListContainer/ListContainer";
import { Link } from "react-router-dom";
import playerContext from "../../context/playerContext";
import { useContext } from "react";

interface AlbumSliderProps {
  tracks: any[];
}

function AlbumSlider({ tracks }: AlbumSliderProps) {
  const { setCurrentSong, currentSong, setPlaylist } =
    useContext(playerContext);
  return (
    <ListContainer
      title="PlayLists for you"
      isScrollable
      id="spotify:playlist:37i9dQZF1DWZCOSaet9tpB"
    >
      <div className="flex gap-4 overflow-x-scroll mt-5 pb-4 album-slider">
        {[...Array(10)].map((_, i) => (
          <div
            key={i}
            className="relative w-40 aspect-square rounded-lg overflow-hidden flex-shrink-0 group cursor-pointer"
            onClick={() => {
              setPlaylist(tracks);
              setCurrentSong(i);
            }}
          >
            <img
              src={tracks[i]?.album.images[0].url}
              alt={tracks[i]?.album.name}
              className="absolute top-0 left-0 w-full h-full object-cover transition-transform transform group-hover:scale-110 duration-300 ease-in-out"
            />
            <h3 className="text-white font-bold absolute top-0 left-0 p-2 text-shadow">
              {tracks[i]?.album.name}
            </h3>
            <p className="text-sm absolute bottom-0 left-0 text-white p-2 bg-black bg-opacity-50 w-full transition-colors group-hover:bg-opacity-80 duration-300 ease-in-out truncate">
              {tracks[i]?.artists.map((artist: any) => artist.name).join(", ")}
            </p>
          </div>
        ))}
      </div>
    </ListContainer>
  );
}

export default AlbumSlider;
