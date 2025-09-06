import React, { useEffect, useState  } from "react";
import axios from "axios" ;

function Recommendations({userId,onLogout}) {
    const[recs,setRecs] = useState([]);

    useEffect(() => {
        async function fetchRecs() {
            try{
                const res = await axios.get(
                    `http://127.0.0.1:5000/recommend?user_id=${userId}&top_n=5`
                );
                setRecs(res.data);
            } catch(err) {
                console.log("Error Fetching recommendations", err)
            }
        }
        fetchRecs();
    }, [userId]);

    return (
    <div className="p-6">
        <div className="flex justify-between items-center">
        <h1 className="text-xl font-bold">Recommendations for {userId}</h1>
        <button onClick={onLogout} className="bg-red-500 text-white px-3 py-1 rounded">
            Logout
        </button>
        </div>

        <ul className="mt-6 space-y-3">
        {recs.map((item, index) => (
            <li
            key={index}
            className="border p-4 rounded shadow hover:bg-gray-50"
            >
            <p><strong>Product ID:</strong> {item.product_id}</p>
            <p><strong>Score:</strong> {item.score.toFixed(2)}</p>
            </li>
        ))}
        </ul>
    </div>
    );
}
export default Recommendations;