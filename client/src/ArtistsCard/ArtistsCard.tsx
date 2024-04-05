import ListContainer from "../components/ListContainer/ListContainer";

interface ArtistsCardProps {
  artists: any[];
}

function ArtistsCard({ artists }: ArtistsCardProps) {
  return (
    <ListContainer title={"Popular Artists"} isScrollable>
      <div className="flex gap-8 overflow-x-scroll mt-5 pb-4 px-5 album-slider">
        {[...Array(10)].map((_, i) => (
          <div
            key={i}
            className="relative w-36 flex flex-col flex-shrink-0 gap-5 cursor-pointer group"
          >
            <div className="rounded-full overflow-hidden">
              <img
                src={artists[i]?.images[0].url}
                alt="Artist"
                className="w-full aspect-square object-cover rounded-full transition-transform transform group-hover:scale-110 duration-300 ease-in-out"
              />
            </div>
            <h3 className="text-white font-bold text-center text-shadow">
              {artists[i]?.name}
            </h3>
          </div>
        ))}
      </div>
    </ListContainer>
  );
}

export default ArtistsCard;
