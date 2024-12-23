import { FormEvent, useState } from 'react';
import { Detail } from '../../components/detail';
import { useQuery } from '@tanstack/react-query';


const fetchFn = async (address: string) => {
    console.log('fetchFn... *****', address);
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
        <>
            <div className='mb-5'>
                <form onSubmit={onSubmit}>
                    <input
                        type='text'
                        value={address}
                        onChange={(e) => setAddress(e.target.value)}
                        placeholder='Address'
                    />
                    <button type='submit'>Submit</button>
                </form>
            </div>
            {isFetching ? 'Loading...' : null}
            {!isFetching && data ? 
                <div className='grid grid-cols-2 gap-10'>
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
        </>
    )
}
