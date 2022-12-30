import React from 'react'
import icon1 from '../Assets/man-head.svg'

const Team = () => {

    const nameTeam = [
        {
            id:1,
            nama:'Dikka',
            nim:'2108561002',
            image:'https://avatars.githubusercontent.com/u/97956426?v=4'
        },
        {
            id:2,
            nama:'Oskar',
            nim:'2108561007',
            image:'https://avatars.githubusercontent.com/u/66617793?v=4'
        },
        {
            id:3,
            nama:'Hidayat',
            nim:'2108561033',
            image:'https://avatars.githubusercontent.com/u/107021158?v=4'
        },
        {
            id:4,
            nama:'Bagus Ari',
            nim:'2108561044',
            image:'https://avatars.githubusercontent.com/u/25946873?v=4'
        }
    ]

    return (
        <>
            <div className="w-full bg-white md:rounded-t-[80px] pt-10 pb-10">
                <div className="font-abc mx-auto text-center justify-center items-center">
                    <h1 className="text-darked text-3xl font-semibold">Anggota Kelompok</h1>
                </div>

                <div className="flex flex-wrap font-[Poppins] justify-center mt-10">
                    {nameTeam.map(({id, nama, nim, image}) => (
                        <div key={id} className="flex flex-col bg-whitening rounded-lg w-full m-6 overflow-hidden lg:w-[20%] border-2 border-gray-100 transition-all hover:bg-graying hover:text-white hover:duration-300 hover:transition-all">
                            <img className="md:h-30 mx-6" src={image} alt="gambar" />
                            <div className="text-center px-2 text-darked pt-2 pb-2">
                                <h2 className="font-semibold text-2xl">{nama}</h2>
                                <h4 className="font-medium text-lg">{nim}</h4>
                            </div>
                        </div>
                    ))}
                </div>
            </div>        
        </>
    )
}

export default Team