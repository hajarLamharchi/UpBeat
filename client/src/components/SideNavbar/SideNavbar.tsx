import { FaHome, FaHeart, FaSearch } from "react-icons/fa";
import { Link } from "react-router-dom";
import { BiSolidPlaylist } from "react-icons/bi";
import { IoMdLogIn, IoMdLogOut } from "react-icons/io";
import { IoPerson, IoPersonAdd } from "react-icons/io5";
import "./SideNavbar.css";

interface SideNavbarProps {
  isLoggedIn: boolean;
}

function SideNavbar() {
  const logOut = () => {
    sessionStorage.removeItem("access_token")
    sessionStorage.removeItem("refresh_token")
  }

  return (
    <div className="navbar-container">
      <nav className="navbar">
        <h2>UpBeat</h2>
        <ul className="navbar-items">
          <li>
            <Link to="/home" className="item">
              <FaHome />
              <h3>Home</h3>
            </Link>
          </li>
          <li>
            <Link to="/search" className="item">
              <FaSearch />
              <h3>Search</h3>
            </Link>
          </li>
          <li>
            <Link to="/favory" className="item">
              <FaHeart />
              <h3>Favory</h3>
            </Link>
          </li>
          <li>
            <Link to="/playlist" className="item">
              <BiSolidPlaylist />
              <h3>Playlist</h3>
            </Link>
          </li>
        </ul>
        <div className="navbar-login-section navbar">
          {sessionStorage.getItem('access_token')  ? (
            <ul className="navbar-items">
              <li>
                <Link to="/account" className="item">
                  <IoPerson />
                  <h3>My Account</h3>
                </Link>
              </li>
              <li>
                <Link to="/login" className="item" onClick={logOut}>
                  <IoMdLogOut />
                  <h3>Logout</h3>
                </Link>
              </li>
            </ul>
          ) : (
            <ul className="navbar-items">
              <li>
                <Link to="/signup" className="item">
                  <IoPersonAdd />
                  <h3>Sign up</h3>
                </Link>
              </li>
              <li>
                <Link to="/login" className="item">
                  <IoMdLogIn />
                  <h3>Log in</h3>
                </Link>
              </li>
            </ul>
          )}
        </div>
      </nav>
    </div>
  );
}

export default SideNavbar;
