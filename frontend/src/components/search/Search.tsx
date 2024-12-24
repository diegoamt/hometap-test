import { FormEvent, useState } from 'react';
import { Detail } from '../../components/detail';
import { useQuery } from '@tanstack/react-query';


const fetchFn = async (address: string) => {
    const url = `http://localhost:8000/api/v1/property-details/?address=${address}`;
    const response = await fetch(url, {
        headers: { 'Content-Type': 'application/json' },
    });
    const result = await response.json();
    return result;
};

export function Search() {
    const [address, setAddress] = useState('');

    const { isFetching, error, data, refetch } = useQuery({
        queryKey: ['fetchDetails'],
        queryFn: () => fetchFn(address),
        enabled: false,
    });

    if (error) return `An error has occurred: ${error.message}`;

    const onSubmit = (event: FormEvent) => {
        event.preventDefault();
        refetch();
    }

    return (
        <section>
            <div className='mb-5 flex items-center w-full justify-center'>
                <form className='flex flex-col gap-5 items-center' onSubmit={onSubmit}>
                    <input
                        className='px-4 py-2 min-w-[400px]'
                        name='address'
                        type='text'
                        value={address}
                        onChange={(e) => setAddress(e.target.value)}
                        placeholder='Enter address...'
                    />
                    <button
                        className='bg-blue-700 px-12 py-3 rounded-md text-white font-bold hover:bg-blue-800 disabled:bg-gray-600 disabled:cursor-not-allowed'
                        type='submit'
                        disabled={isFetching}
                    >
                        Submit
                    </button>
                </form>
            </div>
            {isFetching ? 'Loading...' : null}
            {!isFetching && data ? 
                <div className='grid grid-cols-2 gap-10 mb-12'>
                    <Detail
                        title='Provider 1'
                        propertyDetails={data.provider_1} 
                    />
                    <Detail
                        title='Provider 2'
                        propertyDetails={data.provider_2} 
                    />
                </div>
            : null}
        </section>
    )
}
