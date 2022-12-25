import React from 'react'

const Navbar = () => {

  const Links = [
    {
      id: 1,
      link: 'home'
    },
    {
      id: 2,
      link: 'team'
    },
    {
      id: 3,
      link: 'parsing'
    }
  ]


  return (
    <>
      <div className="flex justify-between items-center w-full h-16 px-5 bg-darked shadow-lg font-abc max-w-[1240px] mx-auto">
        <div className="font-bold text-xl cursor-pointer flex items-center">
          <span className="mr-3 pt-2 text-whitening">
            <ion-icon name="desktop-outline"></ion-icon>
          </span>
          <h1 className="hover-scale-105 duration-200 w-full text-[#00df9a]">Teori Bahasa & Otomata</h1>
        </div>
        <ul className="hidden md:flex">
          {Links.map(({id, link}) => (
            <li key={id} className="px-5 cursor pointer capitalize font-medium text-white hover-scale-105 duration-200 cursor-pointer">{link}</li>
          ))}
        </ul>
      </div>
    </>
  )
}

export default Navbar