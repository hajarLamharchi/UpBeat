import TrackCard from "../TrackCard/TrackCard";
import "./NewReleasedItems.css";
import { useState, useEffect, useRef, useContext } from "react";
import axios from "axios";
import { set } from "react-hook-form";
import SkeletonCards from "../SkeletonCards/SkeletonCards";
import playerContext from "../../context/playerContext";

function NewReleasedItems({ clickedLeft, clickedRight }: any) {
  const [apiData, setApiData] = useState<any>();
  const [isLoading, setIsLoading] = useState(true);
  const { setPlaylist } = useContext(playerContext);
  const getapi = () => {
    axios
      .get("https://upbeat-server.onrender.com/api/v1/new_release/")
      .then((res) => {
        setApiData(
          res.data.albums.items.map((item: any) => {
            return {
              artist: item.artists[0].name,
              image: item.images[0].url,
              title: item.name,
              link: item.uri,
              alt: item.name,
            };
          })
        );
        setIsLoading(false);
        setPlaylist(res.data.albums.items);
        console.log(res.data.albums.items);
      })
      .catch((err) => {
        console.log(err);
      });
  };
  useEffect(() => {
    getapi();
  }, []);

  const [scrollPosition, setScrollPosition] = useState(0);
  const ref = useRef<HTMLDivElement>(null);

  const scroll_right = () => {
    const amount = 200;
    const container = ref.current;
    if (
      container &&
      container.scrollWidth - container.clientWidth > scrollPosition
    ) {
      container.scrollBy({ top: 0, left: amount, behavior: "smooth" });
      setScrollPosition(scrollPosition + amount);
    }
  };
  const scroll_left = () => {
    const amount = 200;
    const container = ref.current;
    console.log(container?.scrollHeight);
    if (container && scrollPosition > 0) {
      container.scrollBy({ top: 0, left: amount, behavior: "smooth" });
      setScrollPosition(scrollPosition - amount);
    }
  };
  useEffect(() => {
    const container = ref.current;
    if (container) {
      container.scrollTo({ left: scrollPosition, behavior: "smooth" });
    }
  }, [scrollPosition]);

  useEffect(() => {
    ref.current?.addEventListener("wheel", (e) => {
      e.preventDefault();
      if (e.deltaY >= -15 && e.deltaY <= 15) {
        ref.current?.scrollBy({
          top: 0,
          left: e.deltaY * 40,
          behavior: "smooth",
        });
      } else {
        ref.current?.scrollBy({
          top: 0,
          left: e.deltaY * 5,
          behavior: "smooth",
        });
      }
      setScrollPosition(ref.current?.scrollLeft || 0);
    });
  }, []);

  useEffect(() => {
    scroll_left();
  }, [clickedLeft]);

  useEffect(() => {
    scroll_right();
  }, [clickedRight]);

  return (
    <div className="new-relased-items" ref={ref}>
      {isLoading ? (
        <SkeletonCards count={8} />
      ) : (
        apiData?.map((item: any, index: number) => (
          <TrackCard
            key={index}
            id={item.uri}
            link={item.link}
            image={item.image}
            artist={item.artist}
            title={item.title}
            alt={item.alt}
          />
        ))
      )}
    </div>
  );
}

export default NewReleasedItems;
