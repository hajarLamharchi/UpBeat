import "./Home.css";
import SideNavbar from "../../components/SideNavbar/SideNavbar";
import TrackContainer from "../../components/TrackContrainer/TrackContrainer";
import { useState, useEffect, useContext } from "react";
import { MusicData } from "../../global.d";
import playerContext from "../../context/playerContext";
import axios from "axios";

// interface HomePageProps {
//   isLoggedIn: boolean;
//   usename: string;
// }

function HomePage() {
  const [currentUser, setCurrentUser] = useState()
  const [songData, setSongData] = useState<MusicData>({
    "New Released": [],
    "Popular Artists": [],
    "Popular Tracks": [],
  });

  const { setPlaylist } = useContext(playerContext);

  useEffect(() => {
    const fetchData = async () => {
      let response = await (await fetch("../../api/songData.json")).json();

      const response1 = Object.keys(response)
        .map((key) => response[key])
        .flat();

      setPlaylist(response1);
      return response;
    };

    fetchData().then((data) => {
      setSongData(data);
    });
    axios.get('https://upbeat-server.onrender.com/api/v1/user/current_user', {
      headers: {
        Authorization: `Bearer ${sessionStorage.getItem('access_token')}`,
      },
    })
      .then((res) => {
        setCurrentUser(res?.data?.user?.firstname)
      })
      .catch((err) => console.log(err))
  }, []);

  return (
    <div className="homepage-container relative">
      <SideNavbar />
      <div className="homepage-content">
        {sessionStorage.getItem('access_token') && <h1>Welcome, {currentUser}</h1>}
        <TrackContainer />
      </div>
    </div>
  );
}

export default HomePage;
