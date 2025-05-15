import { useState } from 'react'
import useAuth from '../hooks/useAuth'

export default function Home() {
  const [prompt, setPrompt] = useState('')
  const [projectName, setProjectName] = useState('')
  const { user, login, logout } = useAuth()
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)

  const handleGenerate = async (e) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      const res = await fetch('/api/projects', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${user.token}`
        },
        body: JSON.stringify({
          name: projectName,
          prompt: prompt
        })
      })
      
      const data = await res.json()
      setResult(data)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <header>
        {user ? (
          <button onClick={logout}>Logout</button>
        ) : (
          <button onClick={login}>Login</button>
        )}
      </header>

      <main>
        <h1>AI Website Generator</h1>
        
        <form onSubmit={handleGenerate}>
          <input
            type="text"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            placeholder="Project Name"
            required
          />
          
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Describe your website..."
            required
          />
          
          <button type="submit" disabled={!user || loading}>
            {loading ? 'Generating...' : 'Generate'}
          </button>
        </form>

        {result && (
          <div className="result">
            <h3>Generated Project</h3>
            <a href={result.downloadUrl}>Download</a>
          </div>
        )}
      </main>
    </div>
  )
}