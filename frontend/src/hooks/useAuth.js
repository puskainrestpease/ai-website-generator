import { useState, useEffect } from 'react'

export default function useAuth() {
  const [user, setUser] = useState(null)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if(token) setUser({ token })
  }, [])

  const login = async () => {
    const res = await fetch('/api/auth/login', { method: 'POST' })
    const { token } = await res.json()
    localStorage.setItem('token', token)
    setUser({ token })
  }

  const logout = () => {
    localStorage.removeItem('token')
    setUser(null)
  }

  return { user, login, logout }
}