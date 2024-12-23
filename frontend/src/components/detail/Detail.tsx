interface DetailsProps<T> {
    title: string;
    propertyDetails: Record<string, T>;
}

export function Detail<T,>({ title, propertyDetails }: DetailsProps<T>) {
    return (
        <div className="p-10 shadow-lg bg-white rounded-lg">
            <h2 className="font-bold text-2xl mb-5">{title}</h2>
            <ul className="flex gap-3 flex-col">
                {Object.entries(propertyDetails).map(([key, value]) => (
                    <li key={key} className="flex gap-3 w-full rounded bg-gray-100 py-1 px-3">
                        <div className="font-semibold">{key}:</div>
                        <div>{String(value)}</div>
                    </li>
                ))}
            </ul>
        </div>
    )
}