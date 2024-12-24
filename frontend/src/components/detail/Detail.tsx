interface DetailsProps<T> {
    title: string;
    propertyDetails: Record<string, T>;
}

export function Detail<T,>({ title, propertyDetails }: DetailsProps<T>) {

    const formatLabel = (value: string) => value.replace(/_/g, " ");

    const formatPrice = (price: number): string => {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 0,
        }).format(price);
    };

    return (
        <div className="p-10 shadow-lg bg-white rounded-lg">
            <h2 className="font-bold text-2xl mb-5">{title}</h2>
            <ul className="flex gap-3 flex-col">
                {Object.entries(propertyDetails).map(([key, value]) => (
                    <li key={key} className="flex justify-between gap-3 w-full rounded bg-gray-100 py-1 px-3">
                        <div className="font-semibold">{formatLabel(key)}:</div>
                        <div>{key === "Sale_Price" ? formatPrice(Number(value)) : String(value)}</div>
                    </li>
                ))}
            </ul>
        </div>
    )
}