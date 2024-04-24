import React from "react";
import '../styles/tailwind.css'

class Footer extends React.Component {
    render() {
        return (
            <div className="flex flex-row justify-evenly bg-black text-red p-8 mt-44">
                <div>
                    Agniv Ganguly
                </div>
                <div>
                    Keshav Kejriwal
                </div>
                <div>
                    Ashesh Banerjee
                </div>
            </div>
        )
    }
}

export default Footer;