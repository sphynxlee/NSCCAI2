import PropTypes from 'prop-types';

export default function ListFrag({ listItems }) {

    return (
        <div>
            <ul>
                {listItems.map((item, index) => (
                    <li key={index}>{item}</li>
                ))}
            </ul>
        </div>
    );
}

ListFrag.propTypes = {
    listItems: PropTypes.array.isRequired,
};