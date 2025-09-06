import React, { useState } from "react";
import Login from "./components/login";
import Recommendations from "./components/Recommendations";

function App() {
  const [userId, setUserId] = useState(null);

  return (
    <div>
      {userId ? (
        <Recommendations userId={userId} onLogout={() => setUserId(null)} />
      ) : (
        <Login onLogin={setUserId} />
      )}
    </div>
  );
}

export default App;
