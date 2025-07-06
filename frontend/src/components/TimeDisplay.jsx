import React from 'react';

function TimeDisplay({ time }) {
  if (time === undefined || time === null) return null;
  return (
    <div className="mt-4">
      <span className="text-sm font-medium text-gray-700">Time to Crack</span>
      <div className="text-lg font-semibold text-blue-700">{time}</div>
    </div>
  );
}

export default TimeDisplay; 