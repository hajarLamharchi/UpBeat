import { WavyBackground } from "./components/wavyBackground";
import Home from "./pages/Home/Home";
import LandingPage from "./pages/LandingPage/LandingPage";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Signup from "./pages/Signup/Signup";
import PlayerState from "./context/playerState";
import Login from "./pages/Login/Login";

const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
  },
  {
    path: "/home",
    element: <Home  />,
  },
  {
    path: "/signup",
    element: <Signup />,
  },
  {
    path: "/login",
    element: <Login />
  }
]);

function App() {
  return (
    <>
      <WavyBackground />
      <PlayerState>
        <RouterProvider router={router} />
      </PlayerState>
    </>
  );
}

export default App;
