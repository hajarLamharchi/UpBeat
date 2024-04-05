import { useContext, useEffect, useState } from "react";
import AlbumSlider from "../../components/AlbumSlider/AlbumSlider";
import SideNavbar from "../../components/SideNavbar/SideNavbar";
import axios from "axios";
import SongList from "../../components/SongList/SongList";
import AlbumGrid from "../../components/AlbumGrid/AlbumGrid";
import ArtistsCard from "../../ArtistsCard/ArtistsCard";
import AudioPlayer from "../../components/AudioPlayer/AudioPlayer";
import playerContext from "../../context/playerContext";

interface PlaylistsProps {
  isLoggedIn: boolean;
  usename: string;
}

function Playlists({ isLoggedIn, usename }: PlaylistsProps) {
  const [myPlaylists, setMyPlaylists] = useState<any>([]);
  const [myPlaylists2, setMyPlaylists2] = useState<any>([]);
  const [myPlaylists3, setMyPlaylists3] = useState<any>([]);
  const [artist, setArtist] = useState<any>([]);

  useEffect(() => {
    axios
      .get(
        "https://upbeat-server.onrender.com/api/v1/playlist/spotify:playlist:37i9dQZF1DWZCOSaet9tpB/tracks"
      )
      .then((response) => {
        // console.log(response.data);
        response.data.map((item: any) => {
          // console.log(item.track);
          setMyPlaylists((prev: any) => [...prev, item.track]);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    axios
      .get("https://upbeat-server.onrender.com/api/v1/new_release/")
      .then((response) => {
        console.log(response.data);
        response.data.albums.items.map((item: any) => {
          setMyPlaylists2((prev: any) => [...prev, item]);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    axios
      .get("https://upbeat-server.onrender.com/api/v1/featured_playlist")
      .then((response) => {
        // console.log(response.data);
        response.data.playlists.items.map((item: any) => {
          // console.log(item);
          setMyPlaylists3((prev: any) => [...prev, item]);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  useEffect(() => {
    axios
      .get("https://upbeat-server.onrender.com/api/v1/popular_artists")
      .then((response) => {
        // console.log(response.data);
        response.data.artists.items.map((item: any) => {
          // console.log(item);
          setArtist((prev: any) => [...prev, item]);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className="homepage-container relative">
      <SideNavbar isLoggedIn={isLoggedIn} />
      <div className="w-[90%] h-svh ml-1 p-5 overflow-auto">
        <div className="bg-clip-padding backdrop-filter backdrop-blur-md bg-opacity-30 border border-slate-700  bg-gray-800 mx-2 text-white py-4 pb-5 px-5 rounded-lg w-full min-h-[94vh] flex flex-col gap-10">
          <AlbumSlider tracks={myPlaylists} />
          <SongList songs={myPlaylists2} />
          <AlbumGrid albums={myPlaylists3} />
          <ArtistsCard artists={artist} />
        </div>
      </div>
    </div>
  );
}

export default Playlists;
