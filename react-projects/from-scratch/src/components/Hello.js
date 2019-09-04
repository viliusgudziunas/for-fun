import React from "react";

const Hello = () => {
  // return (
  //   <div className="dummy-class">
  //     <h1>Hello Vilius</h1>
  //   </div>
  // );
  return React.createElement(
    "div",
    { id: "hello", className: "dummy-class" },
    React.createElement("h1", null, "Hello Vilius")
  );
};

export default Hello;
