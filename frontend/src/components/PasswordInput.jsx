import React from 'react';

function PasswordInput({ password, setPassword }) {
  return (
    <input
      type="password"
      value={password}
      onChange={e => setPassword(e.target.value)}
      placeholder="Enter your password"
      className="w-full px-4 py-2 border-2 border-purple-300 rounded-lg focus:outline-none focus:border-purple-500 transition"
    />
  );
}

export default PasswordInput; 