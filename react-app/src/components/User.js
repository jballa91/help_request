import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function Student() {
  const [user, setStudent] = useState({});
  // Notice we use useParams here instead of getting the params
  // From props.
  const { userId } = useParams();

  useEffect(() => {
    if (!userId) {
      return;
    }
    (async () => {
      const response = await fetch(`/api/users/${userId}`);
      const user = await response.json();
      setStudent(user);
    })();
  }, [userId]);

  if (!user) {
    return null;
  }

  return (
    <ul>
      <li>
        <strong>Student Id</strong> {userId}
      </li>
      <li>
        <strong>Studentname</strong> {user.username}
      </li>
      <li>
        <strong>Email</strong> {user.email}
      </li>
    </ul>
  );
}
export default Student;
