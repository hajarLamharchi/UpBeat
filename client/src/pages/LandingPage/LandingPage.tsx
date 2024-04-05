import { Link } from "react-router-dom";
import "./LandingPage.css";

const LandingPage = () => {
    return (
        <div className="text-center flex flex-col justify-center items-center h-screen relative">
            <p className="text-6xl md:text-8xl lg:text-9xl text-white font-bold inter-var">
                UpBeat
            </p>
            <p className="text-base md:text-lg mt-4 text-white font-normal inter-var">
                Dance To Your Own Beat With UpBeat
            </p>
            <div className="link-container hover:scale-110">
                <Link
                    to="/home"
                    className="landing-page-link text-base text-white font-bold">
                    Tune In
                </Link>
            </div>
        </div>
    );
};

export default LandingPage;
