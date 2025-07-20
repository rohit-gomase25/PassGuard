import React, { useState, useEffect } from 'react';
import PasswordInput from './components/PasswordInput';
import StrengthMeter from './components/StrengthMeter';
import TimeDisplay from './components/TimeDisplay';
import Results from './components/Results';
import { analyzePassword } from './services/api';

function App() {
  const [password, setPassword] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!password) {
      setResult(null);
      setError(null);
      return;
    }
    const handler = setTimeout(async () => {
      setLoading(true);
      setError(null);
      try {
        const res = await analyzePassword(password);
        setResult(res);
      } catch (err) {
        setError('Error analyzing password');
        setResult(null);
      }
      setLoading(false);
    }, 500);
    return () => clearTimeout(handler);
  }, [password]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-100 flex items-center justify-center p-4">
      <div className="bg-white shadow-xl rounded-xl p-8 max-w-md w-full space-y-6">
        <h1 className="text-3xl font-bold text-center text-purple-700 mb-4">Password Analyzer AI</h1>
            <div className="flex items-start gap-4">
              <div className="flex-1 relative">
                <PasswordInput password={password} setPassword={setPassword} />
              </div>
              {result && password && (
                <div className="w-80 p-4 bg-yellow-100 border-l-4 border-yellow-500 text-yellow-800 rounded shadow-lg">
                  <div className="font-semibold mb-2">Strong Password Suggestion:</div>
                  <div className="mb-2">{result.suggestion ? result.suggestion : "No suggestion returned from Gemini API."}</div>
                  <div className="mt-2 text-sm text-gray-700">{result.explanation}</div>
                </div>
              )}
            </div>
        {loading && <p className="text-blue-500 text-center animate-pulse">Analyzing...</p>}
        {error && <p className="text-red-500 text-center">{error}</p>}
        <StrengthMeter strength={result?.strength} />
        <TimeDisplay time={result?.time_to_crack} />
        <Results result={result} />
      </div>
    </div>
  );
}

export default App; 