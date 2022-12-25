import React from 'react'
import icon1 from '../Assets/man-head.svg'

const Team = () => {

    const nameTeam = [
        {
            id:1,
            nama:'Dikka',
            nim:'2108561002',
        },
        {
            id:2,
            nama:'Oskar',
            nim:'2108561007',
        },
        {
            id:3,
            nama:'Hidayat',
            nim:'2108561033',
        },
        {
            id:4,
            nama:'Bagus Ari',
            nim:'2108561044',
        }
    ]

    return (
        <>
            <div className="w-full min-h-screen bg-white md:rounded-t-[80px]">
                <div className="font-abc pt-12 mx-auto text-center justify-center items-center">
                    <h1 className="text-darked text-3xl font-semibold">Anggota Kelompok</h1>
                </div>

                <div className="flex flex-wrap font-[Poppins] justify-center mt-5">
                    {nameTeam.map(({id, nama, nim}) => (
                        <div key={id} className="flex flex-col bg-whitening rounded-lg shadow-md w-[30%] m-6 overflow-hidden sm:w-52px border-2 border-graying transition-all hover:bg-graying hover:text-white hover:duration-300 hover:transition-all">
                            <img className="md:h-24 m-6" src={icon1} alt="gambar" />
                            <div className="text-center px-2 text-darked pt-2 pb-2">
                                <h2 className="font-bold text-2xl">{nama}</h2>
                                <h4 className="font-medium text-lg">{nim}</h4>
                            </div>
                        </div>
                    ))}
                </div>
            </div>



            {/* <div className="w-full h-96 bg-white md:rounded-t-[80px]">
                <div className="font-abc pt-8 mx-auto text-center justify-center items-center">
                    <h1 className="text-darked text-2xl font-semibold">Anggota Kelompok</h1>
                </div>
                <div className="flex mx-auto gap-8 max-w-5xl font-[Poppins] mt-5 justify-center items-center">
                    {nameTeam.map(({id, nama, nim, gambar}) => (
                        <div key={id} className="bg-darked p-6 rounded-lg">
                            <img className="h-40 mx-auto" src={gambar} alt="gambar" />
                            <div className="text-whitening text-center pt-4">
                                <h2 className="font-semibold text-2xl">{nama}</h2>
                                <h4 className="text-medium">{nim}</h4>
                            </div>
                        </div>
                    ))}
                </div>
            </div> */}


            {/* <div className="max-w-[1240px] w-full min-h-screen bg-white p-6 pt-20">
                <h2 className="font-bold text-4xl text-center text-[#00df9a] pb-2">TEAMS</h2>
                <p className="font-medium text-lg text-gray-500 text-center pb-8">Identitas Anggota Kelompok 1</p>

                <div className="flex">
                    {nameTeam.map(({id, nama, nim, gambar}) => (
                        <div key={id} className="flex flex-col rounded-lg shadow-md w-full m-2 text-bold">
                            <img className="h-full m-4" src={gambar} alt="" />
                            <h2 className="text-center px-2 font-bold text-xl">{nama}</h2>
                            <h4 className="text-center px-2 mb-4 ">{nim}</h4>
                        </div>
                    ))}
                </div>
            </div> */}

        
        </>
    )
}

export default Team