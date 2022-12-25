import React from 'react'


const Hero = () => {

  return (
    <>
      <div className="w-full h-[80vh]">
        <div className="pt-12 mx-auto text-center justify-center items-center">
          <h1 className="font-abc text-whitening text-3xl font-semibold">Parsing Kalimat</h1>
        </div>
        
        <div className="mt-10 text-[Poppins] md:ml-64 md:mr-64 ml-10 mr-10">
          <p className="text-graying text-lg font-medium pb-2">Kalimat Bahasa Indonesia</p>
          <form>
            <input type="text" placeholder="Input String Disini" className="text-gray-800 border-2 border-graying px-3 py-3 font-light rounded-lg text-md w-full"/>
            <div className="flex pt-4 items-center justify-center">
              <button type="submit" className="text-white bg-graying px-6 py-3 rounded-lg font-medium">Parsing</button>
            </div>
          </form>
          <p className="text-graying text-lg font-medium mt-12">Hasil Pengecekan</p>
        </div>
      </div>

    </>
  )
}

export default Hero