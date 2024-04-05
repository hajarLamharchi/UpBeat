import { FaSearch } from 'react-icons/fa'
import SideNavbar from '../../components/SideNavbar/SideNavbar'
import "./Search.css"
import { useState } from 'react'
import axios from 'axios'
import { FaPlay, FaRegHeart } from "react-icons/fa";

function Search() {
    const [search, setSearch] = useState('')
    const [searchResult, setSearchResult] = useState([])

    const handleSearch = (event: React.KeyboardEvent<HTMLInputElement>) => {
        if (event.key === "Enter") {
            axios.get(`https://upbeat-server.onrender.com/api/v1/search?query=${search}`)
                .then(res => {
                    console.log(res.data.results)
                    setSearchResult(res.data.results)
                })
                .catch(err => console.log(err))
        }
    }

    return (
        <div className='search-container relative'>
            <SideNavbar />
            <div className="search-content">
                <div className="search-input">
                    <FaSearch id='search-icon' />
                    <input type="text"
                        placeholder='Search...'
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        onKeyDown={handleSearch} />
                </div>
                <div className="search-result">
                    {searchResult.length > 0 && (
                        searchResult.map(result => (
                            <div className="result">
                                <img src={result.album_image} alt="img" />
                                <FaPlay id="play-icon"/>
                                <div className="result-info">
                                    <h3>{result.song_name}</h3>
                                    <h5>{result.artist}</h5>
                                </div>
                                <FaRegHeart id='heart-icon'/>
                            </div>
                        ))
                    )}
                </div>
            </div>
        </div>
    )
}

export default Search