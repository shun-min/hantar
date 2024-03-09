import React from 'react'

const HOSTNAME = "http://127.0.0.1:8000"

const getContents = async () => {
    const result = await fetch(`${HOSTNAME}/contents`);

    if (!result.ok) {
        throw new Error("Couldn't fetch content list")
    }
    return result.json()
}

const Contents = async () => {
  const contents = await getContents();
  console.log(contents["files"])
  return (
    <>
      {
        contents["files"].map( (item: string) => {
          console.log(typeof(item))
          return (
              <li>
                <a href='/download'>{item}</a>
              </li>
          )
        })
      }

    </>
  )
}

export default Contents;