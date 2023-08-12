import React from 'react'
import {useAuth0} from '@auth0/auth0-react'
import {Link} from 'react-router-dom'

const Landing = () => {
  const {logout} = useAuth0();
  const { user, isAuthenticated, isLoading } = useAuth0();
  const {loginWithRedirect} = useAuth0();
  return (
    <div className='p-4'>
   <div className='bg-gray-900 flex p-2 justify-between items-center rounded-full'>
   <h1 className='text-white font-white text-3xl px-4'>ENERGYLO</h1>
   
   
   {
    isAuthenticated?(
      <div className='flex gap-3'>
      <Link to="/buy"> <button className='text-white font-white text-xl'>Buy</button></Link>
  <Link to="/sell"> <button className='text-white font-white text-xl'>Sell</button></Link>
      <button onClick={()=>logout()} className='text-xl font-semibold bg-white p-3'>Logout</button>  </div>     ):(
        <button onClick={()=>loginWithRedirect()}
        className=' text-xl font-semibold bg-white p-3'>
        Login</button>    )
  }
   
  
   </div>
    </div>
  )
}

export default Landing
