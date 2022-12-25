import React from 'react'

const Head = () => {
  return (
    <>
      <div className="w-full h-72 flex text-center justify-center items-center bg-white md:rounded-b-full">
        <div className="pb-8 pt-16 font-abc">
          <h1 className="text-darked text-5xl font-bold">Final Project TBO</h1>
          <div className="text-graying font-light p-4 md:text-lg">
            <p>Melakukan Parsing Kalimat dengan Algoritma CYK</p>
            <p className="">Oleh Kelompok 1 ~ Kelas B</p>
          </div>
          <a href="/">
            <button className="bg-graying px-6 py-3 rounded-lg text-white font-medium">Try Now</button>
          </a>
        </div>
      </div>

        {/* <div className="max-w-[800px] w-full min-h-screen mx-auto text-center flex flex-col justify-center font-abc">
          <h1 className="text-darked font-bold text-6xl">Parsing Kalimat</h1>
          <p>Sebuah web untuk melakukan parsing kalimat dengan menggunakan algoritma CYK</p>
          <button className="bg-[#00df9a] w-[200px] rounded-md font-semibold my-6 mx-auto py-3 text-[#000300] text-lg">Let's Start</button>
        </div> */}
    </>
  )
}

export default Head