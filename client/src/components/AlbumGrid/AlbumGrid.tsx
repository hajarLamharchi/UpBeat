import { Link } from "react-router-dom";
import ListContainer from "../ListContainer/ListContainer";
import { FaPlay } from "react-icons/fa";

interface AlbumGridProps {
  albums: any[];
}

export default function AlbumGrid({ albums }: AlbumGridProps) {
  return (
    <ListContainer title="Today's Top Albums">
      <div className="grid grid-cols-fluid gap-4 mt-5 pb-4 place-items-center md:max-h-[35rem] md:overflow-clip">
        {[...Array(10)].map((_, i) => (
          <Link key={i} to={`/playlist/${albums[i]?.uri}`}>
            <div className="rounded-md p-2 hover:bg-gray-700 hover:bg-opacity-40 transition-colors duration-300 ease-in-out cursor-pointer flex flex-col items-center gap-2 group">
              <div className="relative w-44 aspect-square rounded-lg overflow-hidden group cursor-pointer">
                <img
                  src={albums[i]?.images[0].url}
                  alt={albums[i]?.name}
                  className="absolute top-0 left-0 w-full h-full object-cover transition-transform transform group-hover:scale-110 duration-300 ease-in-out"
                />
                <div className="absolute bottom-[-30%] group-hover:bottom-[10%] right-[10%] w-12 h-12 bg-fuchsia-400 rounded-full flex justify-center items-center transition-all duration-300 ease-in-out">
                  <FaPlay className="text-2xl text-white" />
                </div>
              </div>
              <div className="w-44 px-2">
                <h3 className="text-white font-bold text-shadow">
                  {albums[i]?.name}
                </h3>
                <p className="text-sm text-white min-w-3 line-clamp-2 text-shadow">
                  {albums[i]?.description}
                </p>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </ListContainer>
  );
}
