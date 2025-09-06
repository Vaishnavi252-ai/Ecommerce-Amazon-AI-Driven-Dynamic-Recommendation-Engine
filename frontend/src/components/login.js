import React, {useState} from "react";

function Login({onLogin}) {
    const [userId, setUserId] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (userId.trim()){
            onLogin(userId);
        }
    };

    return ( 

        <div className="flex flex-col items-center justify-center min-h-screen bg-blue-100">
        <h1 className="text-2xl font-bold mb-4">Amazon Recommender Login</h1>
        <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow-md">
        <input
            type="text"
            placeholder="Enter your user ID"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            className="border p-2 w-64 mb-4"
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
            Get Recommendations
        </button>
        </form>
    </div>
    );
}
export default Login;