import React from 'react';

const strengthColors = {
  'Very Weak': 'bg-red-400',
  'Weak': 'bg-orange-400',
  'Medium': 'bg-yellow-400',
  'Strong': 'bg-green-400',
  'Very Strong': 'bg-blue-500',
};

function StrengthMeter({ strength }) {
  if (!strength) return null;
  const color = strengthColors[strength] || 'bg-gray-300';
  return (
    <div className="w-full mt-2">
      <div className="flex items-center justify-between mb-1">
        <span className="text-sm font-medium text-gray-700">Strength</span>
        <span className={`text-sm font-bold ${color.replace('bg', 'text')}`}>{strength}</span>
      </div>
      <div className="w-full h-3 bg-gray-200 rounded-full">
        <div className={`h-3 rounded-full transition-all duration-300 ${color}`}
          style={{ width: strength === 'Very Weak' ? '20%' : strength === 'Weak' ? '40%' : strength === 'Medium' ? '60%' : strength === 'Strong' ? '80%' : strength === 'Very Strong' ? '100%' : '0%' }}
        />
      </div>
    </div>
  );
}

export default StrengthMeter; 