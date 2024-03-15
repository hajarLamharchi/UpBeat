import { Link } from "react-router-dom";
import { WavyBackground } from "../../components/wavy-background";
import "./LandingPage.css";

const LandingPage = () => {
    return (
        <WavyBackground className="max-w-4xl mx-auto pb-40">
            <div className="text-center">
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
        </WavyBackground>
    );
};

export default LandingPage;
