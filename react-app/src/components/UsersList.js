import React, { useEffect, useState } from "react";
import { NavLink } from "react-router-dom";

function StudentsList() {
  const [users, setStudents] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/users/");
      const responseData = await response.json();
      setStudents(responseData.users);
    }
    fetchData();
  }, []);

  const userComponents = users.map((user) => {
    return (
      <li key={user.id}>
        <NavLink to={`/users/${user.id}`}>{user.username}</NavLink>
      </li>
    );
  });

  return (
    <>
      <h1>Student List: </h1>
      <ul>{userComponents}</ul>
    </>
  );
}

export default StudentsList;
