import { Link } from "react-router-dom";
import "./TrackCard.css";
import { useContext } from "react";
import playerContext from "../../context/playerContext";

interface TrackCardProps {
  id: number;
  link: string;
  image: string;
  artist: string;
  title: string;
  alt: string;
}

function TrackCard({ id, link, image, artist, title, alt }: TrackCardProps) {
  return (
    <li className={`content-item w-40`}>
      <Link to="/playlist/spotify:playlist:37i9dQZF1DWZCOSaet9tpB">
        <img src={image} alt={alt} className="rounded-sm" />
        <h3>{artist}</h3>
        <h5>{title}</h5>
      </Link>
    </li>
  );
}

export default TrackCard;
