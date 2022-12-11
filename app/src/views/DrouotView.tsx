import {FC, SyntheticEvent, useState} from 'react'

const DrouotView: FC = () => {
  const handleSubmit = async (e: SyntheticEvent) => {
    e.preventDefault()
    const res = await fetch('https://drouot.com')
    console.log(`Response status: ${res.headers}`)
  }
  return (
    <div>
      <iframe src="https://drouot.com">

      </iframe>
      <form onSubmit={handleSubmit} action="https://drouot.com" noValidate>
        <button type="submit">Go</button>
      </form>
      <button onClick={() => fetch('http://127.0.0.1:5000/api/drouot')}>Drouot on server</button>
    </div>
  )
}

export default DrouotView