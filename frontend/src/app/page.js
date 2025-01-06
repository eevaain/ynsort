"use client";

import { useState } from "react";
import InfoPopup from "../components/InfoPopup"; 
import { BlockMath } from "react-katex";

export default function Home() {
  const [solutionVarsInput, setSolutionVarsInput] = useState("i1, i2, i3, i4");
  const [constantsInput, setConstantsInput] = useState(`{
  "IA": 6,
  "Rw": 5.1,
  "Rx": 1.5,
  "Ry": 3.6,
  "Rz": 1.1
}`);
  const [equationsInput, setEquationsInput] = useState(`Rx*(i4-i2) + Rx*i3 = 0
IA = i1 - i2
Rw*i1 + Ry*(i1-i3) + Rx*(i2-i4) = 0
0 + Ry*(i3-i1) + Rz*i3 = 0`);

  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSendRequest = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const solution_variables = solutionVarsInput
        .split(",")
        .map((v) => v.trim())
        .filter(Boolean);

      let constant_variables = {};
      try {
        constant_variables = JSON.parse(constantsInput);
      } catch (jsonError) {
        throw new Error(
          "Failed to parse constant variables. Please ensure it's valid JSON."
        );
      }

      const equations = equationsInput
        .split("\n")
        .map((line) => line.trim())
        .filter(Boolean);

      const data = {
        solution_variables,
        constant_variables,
        equations,
      };

      const res = await fetch("https://ynsortbackend.onrender.com/solve", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!res.ok) {
        throw new Error("Probably check your equations!");
      }

      const json = await res.json();
      setResponse(json);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="flex flex-col items-center justify-center min-h-screen bg-gray-100 text-center p-4 gap-4"
      style={{ fontFamily: "'Roboto Mono', monospace" }}
    >
      <h1 className="text-2xl text-black pb-6">Yₙsort.com [IN BETA]</h1>

      {/* Solution Variables Input */}
      <div className="w-full max-w-md text-left">
        <label className="block text-black mb-1">
          Solution Variables (comma-separated):{" "}
          <InfoPopup infoText="Enter variables separated by commas, e.g: i1, i2." />
        </label>
        <input
          className="w-full p-2 border rounded text-black"
          type="text"
          value={solutionVarsInput}
          onChange={(e) => setSolutionVarsInput(e.target.value)}
        />
      </div>

      {/* Constant Variables Input (JSON) */}
      <div className="w-full max-w-md text-left">
        <label className="block text-black mb-1">
          Constant Variables (JSON):{" "}
          <InfoPopup infoText="Provide constants as a valid JSON object." />
        </label>
        <textarea
          className="w-full p-2 border rounded h-24 text-black"
          value={constantsInput}
          onChange={(e) => setConstantsInput(e.target.value)}
        />
      </div>

      {/* Equations Input (one equation per line) */}
      <div className="w-full max-w-md text-left">
        <label className="block text-black mb-1">
          Equations (New line for each):{" "}
          <InfoPopup infoText="Enter equations, one per line, e.g: Rx*(i4-i2) + Rx*i3 = 0." />
        </label>
        <textarea
          className="w-full p-2 border rounded h-24 text-black"
          value={equationsInput}
          onChange={(e) => setEquationsInput(e.target.value)}
        />
      </div>

      <button
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
        onClick={handleSendRequest}
      >
        Solve!
      </button>

      {loading && <p className="text-gray-600">Loading...</p>}

      {response && (
        <div className="mt-4 p-4 bg-white shadow-md rounded text-left w-full max-w-md">
          <h2 className=" mb-2 text-black">Response:</h2>
          <pre className="text-sm text-gray-800 whitespace-pre-wrap">
            {JSON.stringify(response, null, 2)}
          </pre>

          {/* ONLY render the matrix if response.solution_vector exists */}
          {response.solution_vector && (
            <div style={{ margin: "2rem" }}>
              <h1 className="text-md text-gray-800 whitespace-pre-wrap text-center pb-4">Solution Vector is:</h1>
              {/* Render the solution matrix inline: parse & display as pmatrix */}
              <BlockMath>
                {String.raw`\color{black}{\begin{pmatrix}` +
                  // Transform "Matrix([[0, 0],[0, 0]])" into "0 & 0\\ 0 & 0"
                  response.solution_vector
                    // Remove "Matrix([["
                    .replace(/^Matrix\(\[\[/, "")
                    // Remove the trailing "]])"
                    .replace(/\]\]\)$/, "")
                    // Split rows by "], ["
                    .split("], [")
                    // For each row, split by commas and join with "&"
                    .map((row) =>
                      row
                        .split(",")
                        .map((val) => val.trim())
                        .join(" & ")
                    )
                    // Finally join rows with "\\" for LaTeX
                    .join(" \\\\ ")
                  + String.raw`\end{pmatrix}}`}
              </BlockMath>
            </div>
          )}
        </div>
      )}

      {error && (
        <div className="mt-4 p-4 bg-red-100 text-red-700 rounded w-full max-w-md">
          <h2 className="font-bold mb-2">Error:</h2>
          <p>{error}</p>
        </div>
      )}

      <footer className="mt-8 text-center">
        <p className="text-sm text-gray-600">
          ⭐ If this was helpful,{" "}
          <a
            href="https://github.com/eevaain/ynsort/tree/main"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-500 hover:underline"
          >
            star us on GitHub
          </a>
          !
        </p>
      </footer>
    </div>
  );
}
