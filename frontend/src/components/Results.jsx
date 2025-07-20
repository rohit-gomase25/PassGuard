import React from 'react';

function Results({ result }) {
  if (!result) return null;
  return (
    <div className="mt-6 p-4 bg-purple-50 rounded-lg shadow-inner">
      <h2 className="text-lg font-bold text-purple-700 mb-2">Analysis Summary</h2>
      <div className="text-gray-700">
        <div><span className="font-semibold">Strength:</span> {result.strength}</div>
        <div><span className="font-semibold">Time to Crack:</span> {result.time_to_crack}</div>
        {result.suggestion && result.suggestion.trim() !== "" && (
          <div className="mt-4 p-3 bg-yellow-100 border-l-4 border-yellow-500 text-yellow-800 rounded">
            <span className="font-semibold">Suggestion:</span> {result.suggestion}
          </div>
        )}
      </div>
    </div>
  );
}

export default Results; 